import json

import execjs
# import requests
import aiohttp
import asyncio
from fastapi import APIRouter
from pydantic import BaseModel
from utils import check_proxy
from utils import responses as resp
from utils.responses import response_with

router = APIRouter()
headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://music.163.com',
    'pragma': 'no-cache',
    'referer': 'https://music.163.com/',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}
js_code = open('api_js/netease_music.js', 'r').read()
context = execjs.compile(js_code)


class GetPlaylistsParams(BaseModel):
    searchText: str


class GetSongDetailParams(BaseModel):
    song_searchDetail: str


class GetSongsParams(BaseModel):
    playlistid_searchSongs: str


class GetMusicUrlParams(BaseModel):
    songid_searchSongUrl: str


class GetMisicLyricParams(BaseModel):
    songid_searchSongLyric: str


class GetMusicCommentsParams(BaseModel):
    songid_searchSongComments: str


# 根据歌曲URL下载歌曲
async def download_song(url, songname):  # 无法下载VIP
    print(f'正在下载 <{songname}>')
    async with aiohttp.ClientSession() as session:
        async with session.get(url, proxys=check_proxy()['http']) as response:
            res_cnt = await response.content
    with open(f'{songname}.mp3', 'wb') as f:
        f.write(res_cnt)


async def download_song_by_id(song_id, songname):  # 也不可以下载VIP歌曲 但是VIP尊享歌曲会找不到源地址
    print(f'正在下载 <{songname}>-<{song_id}>')
    url = f'http://music.163.com/song/media/outer/url?id={song_id}'
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, proxy=check_proxy()['http']) as response:
            music_text, music_cnt = await response.text(), response.content
    if '很抱歉，你要查找的网页找不到' in music_text and '404' in music_text:
        print(f'<{songname}>-<{song_id}> 未找到源地址')
    else:
        with open(f'songs/{songname}.mp3', 'wb') as f:
            f.write(music_cnt)


async def get_musicurl_by_songid(songid):
    key_data = context.call('get_keydata', songid)  # 调用js函数,传入music_id参数,但是这个传参我自己没分析出来.是看的别人的思路答案.
    data = {
        'params': key_data.get('encText'),
        'encSecKey': key_data.get('encSecKey'),
    }
    async with aiohttp.ClientSession() as session:
        async with session.post('https://music.163.com/weapi/song/enhance/player/url/v1',
        headers=headers,
        data=data,
        proxy=check_proxy()['http']) as response:
            res_text = await response.text()
    # response = requests.post(
    #     'https://music.163.com/weapi/song/enhance/player/url/v1',
    #     headers=headers,
    #     data=data,
    #     proxies=check_proxy()
    # )
    res_data = json.loads(res_text)
    musicurl = res_data.get('data')
    musicurl = musicurl[0].get('url')
    return musicurl


async def get_lyric_by_songid(songid):  # /weapi/song/lyric
    key_data = context.call('get_lyric_keydata', songid)  # 调用js函数,传入playlist_id参数
    data = {
        'params': key_data.get('encText'),
        'encSecKey': key_data.get('encSecKey'),
    }
    async with aiohttp.ClientSession() as session:
        async with session.post('https://music.163.com/weapi/song/lyric', headers=headers, data=data, proxy=check_proxy()['http']) as response:
            res_text = await response.text()
    # response = requests.post('https://music.163.com/weapi/song/lyric', headers=headers, data=data, proxies=check_proxy())
    data = json.loads(res_text)
    return data['lrc']['lyric']


async def get_comments_by_songid(songid):  # "pageSize":"1000"--js default --> 10
    key_data = context.call('get_comment_keydata', songid)  # 调用js函数,传入playlist_id参数
    data = {
        'params': key_data.get('encText'),
        'encSecKey': key_data.get('encSecKey'),
    }
    async with aiohttp.ClientSession() as session:
        async with session.post('https://music.163.com/weapi/comment/resource/comments/get', headers=headers, data=data, proxy=check_proxy()['http']) as response:
            res_text = await response.text()
    # response = requests.post('https://music.163.com/weapi/comment/resource/comments/get', headers=headers, data=data, proxies=check_proxy())
    data = json.loads(res_text)
    # print(data)
    return data['data']['comments']


async def get_playlists_by_userid(userid):
    key_data = context.call('get_playlist_keydata', userid)  # 调用js函数,传入playlist_id参数
    data = {
        'params': key_data.get('encText'),
        'encSecKey': key_data.get('encSecKey'),
    }
    # 歌单全部评论链接
    # response = requests.post('https://music.163.com/weapi/comment/resource/comments/get', headers=headers, data=data)
    async with aiohttp.ClientSession() as session:
        async with session.post('https://music.163.com/weapi/user/playlist', headers=headers, data=data, proxy=check_proxy()['http']) as response:
            res_text = await response.text()
    # response = requests.post('https://music.163.com/weapi/user/playlist', headers=headers, data=data, proxies=check_proxy())
    # https://music.163.com/weapi/comment/resource/comments/get
    data = json.loads(res_text)
    playlist = data['playlist']
    playlist_dict = dict()
    for index, _ in enumerate(playlist, start=1):
        # print(_['name'], _['id'])
        playlist_dict[index] = {'name': _['name'], 'id': _['id']}
    return playlist_dict


async def get_songs_by_playlistid(playlistid):
    key_data = context.call('get_playlist_detail_keydata', playlistid)  # 调用js函数,传入playlist_id参数
    data = {
        'params': key_data.get('encText'),
        'encSecKey': key_data.get('encSecKey'),
    }
    async with aiohttp.ClientSession() as session:
        async with session.post('https://music.163.com/weapi/v6/playlist/detail',
        headers=headers,
        data=data,
        proxy=check_proxy()['http']) as response:
            res_text = await response.text()
    all_data = json.loads(res_text)
    play_list = all_data['playlist']['tracks']
    all_track_ids = all_data['playlist']['trackIds']
    return all_track_ids


async def get_song_detail_by_id(songid):
    key_data = context.call('get_song_detail_keyword', songid)  # 调用js函数,传入playlist_id参数
    data = {
        'params': key_data.get('encText'),
        'encSecKey': key_data.get('encSecKey'),
    }
    async with aiohttp.ClientSession() as session:
        async with session.post('https://music.163.com/weapi/v3/song/detail',
        headers=headers,
        data=data,
        proxy=check_proxy()['http']) as response:
            res_text = await response.text()
    # response = requests.post(
    #     'https://music.163.com/weapi/v3/song/detail',
    #     headers=headers,
    #     data=data,
    #     proxies=check_proxy()
    # ).json()
    try:
        all_data = json.loads(res_text)  # res_json
        song_detail = all_data['songs']
    except Exception:  # {"msg":"参数错误!","code":400}
        # print(response.text)
        song_detail = []
    return song_detail


async def cloud_search_keyword(keyword):  # 测试搜索最多一次100首
    key_data = context.call('cloud_search_keyword', keyword)  # 调用js函数,传入playlist_id参数
    data = {
        'params': key_data.get('encText'),
        'encSecKey': key_data.get('encSecKey'),
    }
    # params = {
    #     'csrf_token': '9799c863a8262335fdb761ea59a59fe1',
    # }
    # cookies = {
    #     'MUSIC_U': '0098CA3D7238B829356CA549225071DC48B76758D6F436D81602A002EF8272B9B45E71541BB3BD1DF8D98E25E40B21B0FF88AFC8B683439B8D4C756EEB542C89159D3D038D7782857F6F46A4BF68E10BC3074D9A7208BE2FA9FADD5B4179E036205A3C530018AB31ADBA6536C3622165E477AD624AEE2BD384FBC0FBF2E551494732D2EE7A7E2E4C87A2A6362630AC8C2C0849F6612BE4FBDE80FCB0A9C10E46334D75438A34996FAEDD3D0F1D85BFBCC30D2EEF8DDA573653C90E4FE60B073F851C27C58B4A1020EF0A164530247D83A2052BB2FE3FCADE016D9DB650764C5ACDAA185BD52F695827854049E89BE444DC49E183DFF9D016C9549FAD4D96CB851824D430AC6BFE5251CE8FD9B984E1D88C8A48986EAD6ECABECE6C1417E44DF28728FE922A01F5DA3910EBD4E44CF1942A2220F79AE2F2A5CD25C05A928F0DA0B67E9BA3BA07F8E7B229D161FF565EF5AAB02B30E18F38AAC7C8BE74F681E0D4F5',
    # }

    async with aiohttp.ClientSession() as session:
        async with session.post(# cookies=cookies,
        # params=params,
        headers=headers,
        data=data,
        proxy=check_proxy()['http']) as response:
            res_text = await response.text()
    # response = requests.post(
    #     'https://music.163.com/weapi/cloudsearch/get/web',
    #     # cookies=cookies,
    #     # params=params,
    #     headers=headers,
    #     data=data,
    #     proxy=check_proxy()
    # )
    all_data = json.loads(res_text)
    try:
        song_detail = all_data['result']['songs']
    except Exception:
        print(all_data)  # {'code': 50000005}
        quit()
    return song_detail


@router.post('/get_playlists_by_uid')
async def get_playlists_by_uid(playlists_params: GetPlaylistsParams):
    user_id = playlists_params.searchText  # 前端请求的参数
    playlist = await get_playlists_by_userid(user_id)  # 测试获取用户歌单
    # print(playlist)
    value = {'searchResults': [{'id': playlist[j]['id'], 'name': playlist[j]['name']} for j in playlist]}
    return response_with(resp.SUCCESS_200, value=value)


@router.post('/get_song_detail_by_sid')
async def get_song_detail_by_sid(songdetail_params: GetSongDetailParams):
    song_id = songdetail_params.song_searchDetail
    playlist = await get_song_detail_by_id(song_id)  # 测试获取用户歌单
    print(playlist[0])
    value = {'searchResults': playlist[0]}
    return response_with(resp.SUCCESS_200, value=value)


@router.post('/get_songs_by_pid')
async def get_songs_by_pid(songs_params: GetSongsParams):
    song_id = songs_params.playlistid_searchSongs
    playlist = await get_songs_by_playlistid(song_id)  # 测试获取用户歌单
    print(playlist)
    value = {'searchResults': [{'id': j['id'], 'uid': j['uid']} for j in playlist]}
    return response_with(resp.SUCCESS_200, value=value)


@router.post('/get_musicurl_by_sid')
async def get_musicurl_by_sid(music_url_params: GetMusicUrlParams):
    song_id = music_url_params.songid_searchSongUrl
    song_info = await get_musicurl_by_songid(song_id)  # 测试获取用户歌单
    print(song_info)
    value = {'searchResults': song_info}
    return response_with(resp.SUCCESS_200, value=value)


@router.post('/get_musiclyric_by_sid')
async def get_musiclyric_by_sid(music_lyric_params: GetMisicLyricParams):
    song_id = music_lyric_params.songid_searchSongLyric
    song_info = await get_lyric_by_songid(song_id)  # 测试获取用户歌单
    print(song_info)
    value = {'searchResults': song_info}
    return response_with(resp.SUCCESS_200, value=value)


@router.post('/get_musiccomments_by_sid')
async def get_musiccomments_by_sid(music_comments_params: GetMusicCommentsParams):
    song_id = music_comments_params.songid_searchSongComments
    song_info = await get_comments_by_songid(song_id)  # 测试获取用户歌单
    comment_info = [{'commentId': i.get('commentId'),
                     'content': i.get('content'),
                     'beReplied': i.get('beReplied'),
                     'extInfo_endpoint': i.get('extInfo').get('endpoint'),
                     'ipLocation': i.get('ipLocation'),
                     'liked': i.get('liked'),
                     'likedCount': i.get('likedCount'),
                     'time': i.get('time'),
                     'timeStr': i.get('timeStr'),
                     'user_avatarUrl': i.get('user').get('avatarUrl'),
                     'user_followed': i.get('user').get('followed'),
                     'user_isHug': i.get('user').get('isHug'),
                     'nickname': i.get('user').get('nickname'),
                     'userId': i.get('user').get('userId'),
                     'userType': i.get('user').get('userType'),
                     'vipRights': i.get('user').get('vipRights'),
                     'vipType': i.get('user').get('vipType')
                     } for i in song_info]
    # from pprint import pprint
    # pprint(song_info[0])
    print(comment_info)
    value = {'searchResults': comment_info}
    return response_with(resp.SUCCESS_200, value=value)

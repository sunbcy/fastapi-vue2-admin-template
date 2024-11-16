import service from '@/utils/request'

// 搜索URL
export async function searchKeywords(data) {
  return await service({
    url: '/netease_music/get_playlists_by_uid',
    method: 'post',
    data
  })
}

export async function songsearchKeywords(data) {
  return await service({
    url: '/netease_music/get_song_detail_by_sid',
    method: 'post',
    data
  })
}

export async function pid_searchKeyword(data) {
  return await service({
    url: '/netease_music/get_songs_by_pid',
    method: 'post',
    data
  })
}

export async function sid_searchUrl(data) {
  return await service({
    url: '/netease_music/get_musicurl_by_sid',
    method: 'post',
    data
  })
}

export async function sid_searchLyric(data) {
  try {
    return await service({
      url: '/netease_music/get_musiclyric_by_sid',
      method: 'post',
      data
    }) // 假设 response.data 是你期望的返回数据
  } catch (error) {
    console.error('获取歌曲歌词失败:', error)
    throw error // 重新抛出错误以便上层处理
  }
}

export async function sid_searchComments(data) {
  try {
    return await service({
      url: '/netease_music/get_musiccomments_by_sid',
      method: 'post',
      data
    }) // 假设 response.data 是你期望的返回数据
  } catch (error) {
    console.error('获取歌曲评论失败:', error)
    throw error // 重新抛出错误以便上层处理
  }
}

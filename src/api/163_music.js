import service from '@/utils/request'

// 搜索URL
export function searchKeywords(data) {
  return service({
    url: '/netease_music/get_playlists_by_uid',
    method: 'post',
    data
  })
}

export function songsearchKeywords(data) {
  return service({
    url: '/netease_music/get_song_detail_by_sid',
    method: 'post',
    data
  })
}

export function pid_searchKeyword(data) {
  return service({
    url: '/netease_music/get_songs_by_pid',
    method: 'post',
    data
  })
}

export function sid_searchUrl(data) {
  return service({
    url: '/netease_music/get_musicurl_by_sid',
    method: 'post',
    data
  })
}

export function sid_searchLyric(data) {
  return service({
    url: '/netease_music/get_musiclyric_by_sid',
    method: 'post',
    data
  })
}

export function sid_searchComments(data) {
  return service({
    url: '/netease_music/get_musiccomments_by_sid',
    method: 'post',
    data
  })
}

import service from '@/utils/request'

// 搜索URL
export function get_block_info() {
  return service({
    url: '/jiucaigongshe/',
    method: 'get'
  })
}

import service from '@/utils/request'

// 搜索URL
export async function get_block_info() {
  return await service({
    url: '/jiucaigongshe/',
    method: 'get'
  })
}

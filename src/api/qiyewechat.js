import service from '@/utils/request'

// 搜索URL
export async function sendText(data) {
  return await service({
    url: '/qiyewechat/send_text',
    method: 'post',
    data
  })
}

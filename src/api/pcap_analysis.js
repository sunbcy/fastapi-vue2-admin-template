import service from '@/utils/request'

// 传递名单
export function get_analysis_info(data) {
  return service({
    url: '/pcap_analysis/analysis',
    method: 'post',
    data
  })
}

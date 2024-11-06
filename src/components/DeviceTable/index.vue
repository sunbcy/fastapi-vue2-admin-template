<template>
  <div>
    <!-- 显示在线设备数量 -->
    <div class="online-count">
      在线设备数量: {{ onlineDeviceCount }}
    </div>
    <el-table :data="tableData" style="width: 100%; height: 284px; max-height: 284px; overflow-y: auto;">
      <el-table-column prop="deviceName" label="设备名" width="130" />
      <el-table-column prop="ip" label="IP" width="130" />
      <el-table-column prop="mac" label="MAC" width="130" />
    </el-table>
  </div>
</template>

<script>
import { get_lan_info } from '@/api/system_info'

export default {
  name: 'DeviceTable',
  data() {
    return {
      tableData: []
      // tableData: [
      //   { deviceName: '设备1', ip: '192.168.1.1', mac: '00-1A-2B-3C-4D-5E' },
      //   { deviceName: '设备2', ip: '192.168.1.2', mac: '00-1A-2B-3C-4D-5F' },
      //   { deviceName: '设备3', ip: '192.168.1.3', mac: '00-1A-2B-3C-4D-60' },
      //   // 可以继续添加更多设备
      // ]
    }
  },
  computed: {
    onlineDeviceCount() {
      return this.tableData.length
    }
  },
  mounted() {
    // 组件挂载时立即运行一次
    this.get_lan_info_interval()

    // 每隔20s再运行一次
    this.intervalId = setInterval(() => { this.get_lan_info_interval() }, 20 * 1000) // 每隔1min切换一次状态
  },
  beforeDestroy() {
    // 清除定时器，防止内存泄漏
    if (this.intervalId) {
      clearInterval(this.intervalId)
    }
  },
  methods: {
    // handleSetLineChartData(type) {
    //   this.lineChartData = lineChartData[type]
    // }
    get_lan_info_interval() {
      get_lan_info().then(res => {
        this.tableData = res.searchResults
        console.log(this.tableData)
      }).catch(err => {
        console.log(err)
        this.$message.error('服务端异常, 获取LAN host失败!')
      })
    }

  }
}
</script>

<style scoped>
/* 你可以在这里添加样式 */
.online-count {
  margin-top: 0px;
  font-size: 16px;
  color: #333;
}
</style>

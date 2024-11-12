<template>
  <div class="chart-wrapper">
    <pie-chart :fetched-info="fetchedInfo" />
    <!--      <PieChart fetched-info="" />-->
  </div>
  <div>
    <!-- 你的分析结果展示逻辑 -->
    <p>{{ fetchedInfo }}</p>
  </div>
</template>

<script>
import PieChart from './PieChart.vue'

export default {
  components: { PieChart },
  props: {
    id: {
      type: [String, Number],
      required: true
    },
    tableData: {
      type: Array,
      required: true
    }
  }, // ['tableData']
  data() {
    return {
      // 你的数据
      fetchedInfo: ''
    }
  },
  created() {
    this.fetchResult(this.id) // 获取结果数据
  },
  methods: {
    fetchResult(id) {
      // 根据ID调用API获取结果数据
      // 在tableData中查找与提供的ID匹配的项
      // console.log(id);
      // console.log(JSON.stringify(this.tableData));
      const result = this.tableData.find(item => item.id === Number(id))
      // console.log(result);
      if (result) {
        // 如果找到匹配的项，你可以根据你的需求处理result.ret_info
        // console.log(result);
        this.fetchedInfo = result.ret_info
      } else {
        console.error('No matching result found for id:', id)
      }
    }

  }
}
</script>

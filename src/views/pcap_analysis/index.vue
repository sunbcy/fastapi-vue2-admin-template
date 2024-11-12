<template>
  <el-container>
    <el-header>数据包上传 & 分析结果</el-header>
    <el-main>
      <el-row :gutter="20">
        <!-- 文件上传的列 -->
        <el-col :span="12">
          <div class="upload-container">
            <el-upload
              ref="upload"
              class="upload"
              drag
              action="http://127.0.0.1:8000/api/pcap_analysis/upload"
              :on-progress="handleProgress"
              :on-success="handleSuccess"
              :on-error="handleError"
              :file-list="fileList"
              multiple
            > <!-- 这里替换为实际的上传URL -->
              <i class="el-icon-upload" />
              <div class="upload-tip">将文件拖至此处，或<em>点击上传</em></div>
              <el-button slot="trigger" size="small" type="primary">选取文件</el-button>
            </el-upload>
            <!-- 添加进度条 -->
            <el-progress v-show="uploadPercentage > 0" :percentage="uploadPercentage" />
            <el-button
              type="success"
              :disabled="!fileList.length || isUploading"
              @click="startAnalysis"
            >开始分析</el-button>
          </div>
        </el-col>

        <!-- 分析结果的列 -->
        <el-col :span="12">
          <el-table :data="tableData" style="width: 100%">
            <!-- ... 表格列的相关设置 -->
            <el-table-column prop="id" label="ID" width="180" />
            <el-table-column prop="packetName" label="数据包名" width="180" />
            <el-table-column label="分析结果链接" width="180">
              <template slot-scope="scope">
                <!-- <router-link :to="`/result/${scope.row.id}`" :tableData="this.tableData">分析结果</router-link> -->

                <!-- 点击链接时显示对话框 -->
                <el-link @click="showResultDialog(scope.row.id)">查看结果</el-link>

                <!-- 对话框组件 -->
                <el-dialog :visible.sync="dialogVisible" title="详细结果" width="60%">
                  <Result :id="currentId" :table-data="tableData" />
                </el-dialog>

              </template>
            </el-table-column>

          </el-table>
        </el-col>

      </el-row>
    </el-main>
  </el-container>
</template>

<script>
import { get_analysis_info } from '@/api/pcap_analysis'
import Result from './Result.vue'

export default {
  components: {
    Result
  },
  data() {
    return {
      fileList: [],
      uploadPercentage: 0, // 用于存储上传进度的变量
      isUploading: false, // 用于指示是否正在上传的变量
      tableData: [],
      dialogVisible: false, // 控制对话框显示的属性
      currentId: '' // 当前行的ID
    }
  },
  mounted() {
    // 当组件被加载后，获取分析数据
    this.startAnalysis()
  },
  methods: {
    // 显示对话框的方法，同时设置当前行的ID
    showResultDialog(id) {
      this.currentId = id
      this.dialogVisible = true
    },
    handleProgress(event, file, fileList) {
      this.uploadPercentage = Math.floor((event.percent || 0)) // 更新上传进度
    },
    handleSuccess(response, file, fileList) {
      this.$message.success('文件上传成功')
      this.uploadPercentage = 0 // 在上传成功后重置进度
      this.isUploading = false // 标记上传结束
      this.fileList.push({
        name: file.name // 假设文件名是必要的信息
        // url: response.url, // 假设response包含了文件的url
        // 根据你具体的需求，你可能需要添加更多的文件属性
      })
    },
    handleError(err, file, fileList) {
      this.$message.error('文件上传失败')
      this.uploadPercentage = 0 // 在上传失败后重置进度
      this.isUploading = false // 标记上传结束
    },
    async getAnalysisData() {
      const send_data = { 'data': this.fileList }
      try {
        const res = await get_analysis_info(send_data)
        this.tableData = res.data
      } catch (err) {
        console.log(err)
        this.$message.error('服务端异常, 分析失败.')
      }
    },
    startAnalysis() {
      if (this.fileList.length > 0) {
        this.$message.success('开始分析数据包...')
        this.getAnalysisData()
      } else {
        this.$message.warning('请先上传数据包')
      }
    }

  }
}
</script>

  <style scoped>
    .upload-container {
      border: 2px dashed #d9d9d9;
      border-radius: 6px;
      padding: 40px 20px;
      text-align: center;
      transition: border-color .3s;
    }

    .upload-container:hover {
      border-color: #409eff;
    }

    .upload-tip em {
      color: #409eff;
      cursor: pointer;
    }

    .el-progress {
      margin-top: 20px;
    }

    .el-button {
      margin-top: 20px; /* Add some spacing between the upload progress and button */
    }

    /* 将Element UI组件的样式进行适当调整 */
    .el-upload-dragger {
      padding: 16px 0;
    }
  </style>

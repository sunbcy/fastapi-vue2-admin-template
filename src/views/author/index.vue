<template>
    <div class="app-container">
        <!-- 添加作者信息按钮-->
        <el-row :gutter="10" class="mb8">
            <el-col :span="1.5">
                <el-button type="primary" icon="el-icon-plus" size="mini" @click="handleAdd">新增</el-button>
            </el-col>
        </el-row>
        <!--作者信息列表-->
        <el-table :data="tableData" border style="width: 100%">
            <el-table-column prop="id" label="序号" width="180"></el-table-column>
            <el-table-column prop="first_name" label="姓名"></el-table-column>
            <el-table-column prop="last_name" label="笔名"></el-table-column>
            <el-table-column label="操作" width="180" align="center">
                <template slot-scope="scope">
                    <el-button size="mini" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
                    <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
                </template>
            </el-table-column>
        </el-table>
        <!--添加作者信息表单-->
        <el-dialog title="添加作者信息" :visible.sync="centerDialogVisible" width="50%" center>
            <el-form ref="form" :model="form" label-width="80px">
                <el-form-item label="作者姓名">
                    <el-input v-model="form.first_name"></el-input>
                </el-form-item>
                <el-form-item label="作者笔名">
                    <el-input v-model="form.last_name"></el-input>
                </el-form-item>
            </el-form>
            <span slot="footer" class="dialog-footer">
                <el-button @click="cancel">取消</el-button>
                <el-button type="primary" @click="save">确定</el-button>
            </span>
        </el-dialog>
    </div>
</template>
<script>
import {
    createAuthorInfo,
    getAuthorInfo,
    getAuthorInfoById,
    UpdateAuthorInfoById,
    DeleteAuthorInfoById
} from "@/api/author";

export default {
    data() {
        return {
            tableData: [], //页面表格数据,即作者信息列表
            centerDialogVisible: false, //用于控制添加与编辑作者信息表单组件是否显示
            form: { //作者信息
                first_name: "",
                last_name: "",
                // created:""
            }
        };
    },
    methods: {
        //添加按钮事件
        handleAdd() {
            this.centerDialogVisible = true;
        },

        //编辑按钮事件
        handleEdit(index, row) {
            this.centerDialogVisible = true;
            this.title = "编辑作者信息";
            this.form = row;
        },

        //弹窗中的取消按钮事件
        cancel(){
            this.centerDialogVisible = false;
            this.reset();
        },

        //重置表单数据
        reset() {
            this.form = {
                first_name: "",
                last_name: "",
                // created: ""
            };
        },

        //弹窗中的确定按钮,调用接口保存作者信息  !!1、title无法定位, 2、why更新 PUT?
        save() {
            if (this.title === "添加作者信息") {
                this.handleCreate();
                console.log(this.title);
            } else {
                this.handleUpdate();
                console.log(this.title);
            }
            this.centerDialogVisible = false;
            
        },
        handleCreate() {
            createAuthorInfo({
                first_name: this.form.first_name,
                last_name: this.form.last_name,
                // created: this.form.created
            }).then(res => {
                console.log(res);
                if (res.code === "success") {
                    this.$message.success("添加成功");
                    this.getAuthorList();
                } else {
                    this.$message.error("添加失败");
                }
            })
            .catch(err => {
                this.$message.error("服务端异常, 添加失败.");
            });
        },
        handleUpdate() {
            UpdateAuthorInfoById(this.form)
                .then(res => {
                if (res.code === "success") {
                    this.$message.success("更新成功");
                } else {
                    this.$message.error("更新失败");
                }
                })
                .catch(err => {
                this.$message.error("服务端异常，更新失败。");
                });
        },
        handleDelete(index, row) {
            const auhtorId = row.id;
            DeleteAuthorInfoById(auhtorId)
                .then(res => {
                if (res.code === "success") {
                    this.$message.success("删除成功");
                    this.getAuthorList();
                } else {
                    this.$message.error("删除失败");
                }
                })
                .catch(err => {
                this.$message.error("删除失败");
                });
        },
        getAuthorList() {
            getAuthorInfo()
                    .then(res => {
                    if (res.code === "success") {
                        this.tableData = res.authors;
                    } else {
                        this.$message.error("获取信息失败");
                    }
                    })
                    .catch(err => {
                    this.$message.error("服务端异常，请联系管理员解决。");
                    });
            },
    },
    mounted() {
        this.getAuthorList();
    }
}

</script>
<style></style>
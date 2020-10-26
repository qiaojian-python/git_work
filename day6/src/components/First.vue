<template>
<div>
    第一个组件
    <el-button @click="c">按钮</el-button>
    <el-button type="primary" @click="c" >主要按钮</el-button>
    <el-button type="success" @click="c">成功按钮</el-button>
    <el-button type="warning" @click="c" icon="el-icon-edit-outline">警告按钮</el-button>
    <el-button type="danger" @click="c" icon="el-icon-delete">删除按钮</el-button>
    <el-button type="info" @click="c">信息</el-button>

</div>
</template>

<script>
export default {
    name: "First",
    methods:{
        c(){
            this.$store.commit("add_count")
        }
    },
}
</script>

<style scoped>

</style>

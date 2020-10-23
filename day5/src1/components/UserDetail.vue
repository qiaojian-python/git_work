<template>
    <div>
        这是用户详情页 <br>
        用户的id为:{{id}} <br>
        用户的姓名为:{{username}} <br>
        用户的生日为:{{bir}} <br>
        用户的个人信息为:{{content}} <br>
    </div>
</template>

<script>
    export default {
        name: "UserDetail",
        data:function () {
            return{
                id:'',
                username:'',
                bir:'',
                content:'',
            }
        },
        created() {
            this.id = this.$route.params.id
            this.username = this.$route.params.username
            this.bir = this.$route.params.bir
            this.content = this.$route.params.content
        }
    }
</script>

<style scoped>

</style>

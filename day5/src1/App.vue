<template>
    <div id="app">

        <h1>这是主页</h1>
        <router-link to="/home">访问home</router-link>
        <router-link to="/user">访问user</router-link>
        <br>
        组件展示的地方: <br>
                <router-view></router-view>

    </div>

</template>

<script>

    export default {
        name: 'App'
    }
</script>

<style>

</style>

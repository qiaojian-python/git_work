<template>
  <div id="app">
    <h3>用户首页</h3>
      <hr>
      <router-link to="/first">第一个</router-link>
      <router-link to="/second">第二个</router-link>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>

</style>

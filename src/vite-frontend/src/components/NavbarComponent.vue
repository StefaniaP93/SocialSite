<template>
<nav class="navbar navbar-expand-lg navbar-dark bg-dark my-navbar mb-4">
  <div class="container">
    <RouterLink :to="{ name: 'home' }" class="navbar-brand">WebSite</RouterLink>
    
    <div class="collapse navbar-collapse">
      <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <RouterLink :to="{ name: 'question-editor'}" class="btn btn-pink me-2">Fai una domanda</RouterLink>
          
        </li>
        <li class="nav-item">
          <a class="btn btn-outline-primary" href="/accounts/logout/">Logout</a>
        </li>
      </ul>
    </div>
  </div>
</nav>
</template>

<script>
export default {
    name: "NavbarComponent"
}
</script>

<style>
.my-navbar {
    border-bottom: 1px solid #DDD;
}
.navbar-brand {
  font-weight: bold;
  font-size:150%;
}
.navbar-brand:hover {
  color: #b01db0 !important;
}
.btn-pink {
  background-color: #c765e5d5;
  color: white;
}
.btn-pink:hover {
  color: #c765e5d5;
}
</style>
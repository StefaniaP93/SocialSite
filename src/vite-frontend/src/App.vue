<template>
  <div>
    <NavbarComponent />
  </div>
  <RouterView />
</template>

<script>
import { RouterLink, RouterView } from 'vue-router';
import { axios } from "@/common/api.service.js";
import { endpoints } from "@/common/endpoints.js";
import NavbarComponent from "@/components/NavbarComponent.vue";


export default {
  name: "App",
  components: {
    NavbarComponent,
  },
  methods: {
    async setUserInfo() {
      try {
        const response = await axios.get(endpoints["usersDetail"]);
        const requestUser = response.data["username"];
        window.localStorage.setItem("username", requestUser);
      } catch (error) {
        console.log(error);
      }
    }
  },
  created() {
    this.setUserInfo();
  }
};
</script>
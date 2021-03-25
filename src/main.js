import Vue from "vue";
import VueRouter from "vue-router";
import Vuikit from "vuikit";
import VuikitIcons from "@vuikit/icons";
import "@vuikit/theme";

import App from "./App.vue";
import Login from "./components/Login.vue";
import Sistema from "./components/Sistema.vue";

const routes = [
  { path: '/', component: Login },
  { path: '/sistema', component: Sistema },
]
const router = new VueRouter({
  routes 
})

Vue.use(Vuikit);
Vue.use(VuikitIcons);
Vue.use(VueRouter);

Vue.config.productionTip = false;

new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");

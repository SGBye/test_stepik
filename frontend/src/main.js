import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify';
import 'codemirror/lib/codemirror.css'
import VueCodemirror from 'vue-codemirror'

Vue.config.productionTip = false

new Vue({
  VueCodemirror,
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')

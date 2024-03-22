import { createRouter, createWebHistory } from 'vue-router'
import Login from '@/views/login.vue'
import Main from '@/views/main.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/',
      name: 'main',
      component: Main
    }
  ]
})

export default router

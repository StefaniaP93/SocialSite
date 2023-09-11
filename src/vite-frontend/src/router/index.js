import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory("/"),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/question/:slug',
      name: 'question-view',
      component: () => import("../views/QuestionView.vue"),
      props: true
    },
    {
      path: '/ask/:slug?',
      name: 'question-editor',
      component: () => import("../views/QuestionEditor.vue"),
      props: true,
    },
    {
      path: '/:catchAll(.*)',
      name: 'page-not-found',
      component: () => import("../views/NotFound.vue"),
    }
  ]
})

export default router

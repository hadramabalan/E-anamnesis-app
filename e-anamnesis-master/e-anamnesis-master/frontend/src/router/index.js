import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from "../views/Home";
import Landing from "../views/Landing";
import About from "../components/home/About";
import Anamnesis from "../components/home/Anamnesis";
import CurrentIllness from "../components/home/CurrentIllness";
import Family from "../components/anamnesis/Family";
import Personal from "../components/anamnesis/Personal";
import Pharmacological from "../components/anamnesis/Pharmacological";
import Social from "../components/anamnesis/Social";
import Allergies from "../components/anamnesis/Allergies";
import Gynecological from "../components/anamnesis/Gynecological";
import Final from "../components/anamnesis/Final"
import Index from "../components/anamnesis/Index";

import IllnessIndex from '../components/current-illness/Index'
import EditIllness from "../components/current-illness/EditIllness";

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Landing',
    component: Landing
  },
  {
    path: '/home',
    name: 'home',
    component: Home,
    children: [
      {
        path: '',
        component: About
      },
      {
        path: 'about',
        component: About
      },
      {
        path: 'anamnesis',
        component: Anamnesis,
        children: [
          {
            path: '',
            component: Index
          },
          {
            path: 'family',
            component: Family
          },
          {
            path: 'personal',
            component: Personal
          },
          {
            path: 'pharmacological',
            component: Pharmacological
          },
          {
            path: 'social',
            component: Social
          },
          {
            path: 'allergies',
            component: Allergies
          },
          {
            path: 'gynecological',
            component: Gynecological
          },
          {
            path: 'final',
            component: Final
          }
        ]
      },
      {
        path: 'current-illness',
        component: CurrentIllness,
        children: [
          {
            path: '',
            component: IllnessIndex
          },
          {
            path: 'edit',
            component: EditIllness
          },
        ]
      }
    ]
  }
];

const router = new VueRouter({
  mode: 'history',
  routes
});

export default router

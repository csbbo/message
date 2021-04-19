import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)
export const store = ({
  state () {
    return {
      count: 0,
      user: {
        username: '',
      },
    }
  },
  mutations: {
    increment (state) {
      state.count++
    },
    SET_USERNAME(state, user) {
        state.user = user
    }
  }
})

export default new Vuex.Store(store)
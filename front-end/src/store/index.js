import axios from 'axios'
import { createStore } from 'vuex'

export default createStore({
  state: {
    songs: [],
    currentSong: {},
    channel: "",
    currentUrl: "",
    loading: false,
    error: false,
  },
  mutations: {
    changeSongs(state, newSongs) {
      state.songs = newSongs
      state.loading = false
    },
    playSong(state, song) {
      state.currentSong = song;
    }, changeUrl(state, url) {
      state.currentUrl = url;
    }
  },
  actions: {
    changeSongs({ commit, state }, channel) {
      state.loading = true;
      state.error = false;
      axios.get(`https://telegram-streaming.herokuapp.com/channel/${channel}/page/1`).then(response => {
        state.channel = channel;
        commit('changeSongs', response.data.files)
      }).catch(err => {
        state.loading = false;
        state.error = true;
        console.log(err)
      })
    },
    playSong({ commit, state }, song) {
      state.currentUrl = `https://telegram-streaming.herokuapp.com/stream/${state.channel}/${song.id}`
      commit('playSong', song);
    },
    changeOffset({ commit }, url) {
      commit('changeUrl', url);
    }
  },
  modules: {
  }
})

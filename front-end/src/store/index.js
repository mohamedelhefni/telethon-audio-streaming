import axios from "axios";
import { createStore } from "vuex";

export default createStore({
  state: {
    songs: [],
    currentSong: {},
    pagination: {},
    endOfFiles: false,
    channel: "",
    currentUrl: "",
    loading: false,
    error: false,
  },
  mutations: {
    changeSongs(state, newSongs) {
      state.songs = newSongs.files;
      state.pagination = newSongs.pagination;
      state.loading = false;
    },
    pushSongs(state, songs) {
      state.songs = state.songs.concat(songs.files)
      state.pagination = songs.pagination
    }
    ,
    playSong(state, song) {
      state.currentSong = song;
    },
    changeUrl(state, url) {
      state.currentUrl = url;
    },
  },
  actions: {
    changeSongs({ commit, state }, channel) {
      state.loading = true;
      state.error = false;
      axios
        .get(
          `https://telegram-streaming.herokuapp.com/channel/${channel}/page/1`
        )
        .then((response) => {
          state.channel = channel;
          commit("changeSongs", response.data);
        })
        .catch((err) => {
          state.loading = false;
          state.error = true;
          console.log(err);
        });
    },
    getNextSongs({ commit, state }) {
      if (state.pagination.next) {
        state.endOfFiles = false;
        axios
          .get(
            `https://telegram-streaming.herokuapp.com/channel/${state.channel}/page/${state.pagination.next}`
          )
          .then((response) => {
            commit("pushSongs", response.data)
          });
      }else {
        state.endOfFiles = true
      }
      console.log("get next songs from store");
    },
    playSong({ commit, state }, song) {
      state.currentUrl = `https://telegram-streaming.herokuapp.com/stream/${state.channel}/${song.id}`;
      commit("playSong", song);
    },
    changeOffset({ commit }, url) {
      commit("changeUrl", url);
    },
  },
  modules: {},
});

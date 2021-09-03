<template>
  <div
    class="
      player
      fixed
      inset-x-0
      bottom-0
      w-full
      text-white text-center
      bg-gray-900
      p-3
    "
  >
    <audio ref="player" :src="currentUrl" preload="metadata"></audio>

    <button @click="togglePlay" class="toggle-play mx-3">
      <SvgIcon
        cls="fill-current text-white cursor-pointer "
        :icon="isPlaying ? 'pause' : 'play'"
      />
    </button>

    <p class="song-name font-bold mb-3 mt-1">
      {{ song.name }}
    </p>
    <div
      v-if="song.time"
      class="time-status mx-auto flex items-center justify-between w-3/4"
    >
      <div class="current-time">{{ formatTime(currentTime) }}</div>
      <div class="progress w-full">
        <input
          type="range"
          class="
            w-3/4
            rounded-lg
            overflow-hidden
            appearance-none
            bg-blue-500
            h-2
          "
          @change="changeProgress(progress)"
          :max="song.time.duration"
          v-model="progress"
        />
      </div>
      <div v-if="song.time" class="">
        {{ formatTime(song.time.duration) }}
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import store from "../store/index";
import SvgIcon from "./SvgIcon.vue";

export default {
  name: "Song Player",
  props: ["song"],
  components: {
    SvgIcon,
  },
  data() {
    return {
      isPlaying: false,
      currentTime: 0,
      progress: 0,
      offset: 0,
      currentSrc: "",
      incTime: null,
    };
  },
  methods: {
    formatTime(secs) {
      let h = Math.floor(secs / 3600);
      let m = Math.floor((secs % 3600) / 60);
      let s = Math.floor((secs % 3600) % 60);
      return `${h >= 10 ? h : "0" + h}:${m >= 10 ? m : "0" + m}:${
        s >= 10 ? s : "0" + s
      }`;
    },
    togglePlay() {
      if (this.isPlaying) {
        this.pause();
      } else {
        this.play();
      }
    },
    play() {
      this.isPlaying = true;
      this.incTime = setInterval(() => {
        this.currentTime++;
        this.progress = this.currentTime;
        if (this.currentTime == this.song.time.duration) {
          this.initSong(this.song);
        }
      }, 1000);
      this.$refs.player.play();
    },
    pause() {
      this.isPlaying = false;
      clearInterval(this.incTime);
      this.$refs.player.pause();
    },
    changeProgress(progress) {
      this.currentTime = progress;
      this.offset = Math.round(progress * this.song.time.bitsPerSecond);
      this.currentSrc = `https://telegram-streaming.herokuapp.com/stream/${store.state.channel}/${this.song.id}?offset=${this.offset}`;
      store.dispatch("changeOffset", this.currentSrc);
      this.pause();
    },

    initSong(song) {
      store.commit(
        "changeUrl",
        `https://telegram-streaming.herokuapp.com/stream/${store.state.channel}/${song.id}`
      );
      store.commit("playSong", song);
      this.currentTime = 0;
      this.progress = 0;
      this.pause();
    },
  },
  computed: {
    ...mapState(["currentUrl"]),
  },
  watch: {
    song: function (newSong) {
      this.initSong(newSong);
    },
  },
};
</script>

<style scoped>
input[type="range"]::-webkit-slider-thumb {
  width: 15px;
  -webkit-appearance: none;
  appearance: none;
  height: 15px;
  cursor: ew-resize;
  background: #fff;
  box-shadow: 405px 0 0 400px #fff;
  border-radius: 50%;
}
</style>
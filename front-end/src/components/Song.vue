<template>
  <div
    class="
      song
      my-2
      transition
      mx-auto
      w-full
      h-full
      pt-3
      bg-white
      shadow
      hover:shadow-lg
      rounded
      flex flex-col
      justify-between
    "
  >
    <div class="song-name font-bold my-2">
      <h2 class="px-2 py-3 text-xl text-gray-700">
        {{ song.name.split("_").join(" ") }}
      </h2>
    </div>
    <div
      class="
        song-props
        my-4
        font-bold
        text-gray-700
        flex
        items-center
        justify-around
      "
    >
      <div class="song-size flex items-center">
        <span>
          {{ (song.size / (1024 * 1024)).toFixed(1) }}
        </span>
        <span class="mx-1">MB</span>
      </div>
      <div class="song-time flex items-center">
        <span class="time mx-2">
          <SvgIcon
            cls="fill-current w-5 h-5 text-gray-700 cursor-pointer "
            icon="time"
          />
        </span>
        <span class="duration">
          {{ formatTime(song.time.duration) }}
        </span>
      </div>
    </div>
    <div class="footer-actions flex items-center justify-center">
      <div
        @click="$store.dispatch('playSong', song)"
        class="
          play
          transition
          cursor-pointer
          border
          group
          hover:text-white
          hover:bg-blue-400
          hover:border-blue-400
          w-1/2
          p-4
          flex
          items-center
          justify-center
        "
      >
        <span class="play-toggle mx-2">
          <SvgIcon
            cls="group-hover:text-white  fill-current w-5 h-5 text-gray-700 cursor-pointer "
            icon="play"
          />
        </span>
        <span class="font-bold">play</span>
      </div>
      <a
        v-bind:href="
          'https://telegram-streaming.onrender.com/download/' +
          $store.state.channel +
          '/' +
          song.id
        "
        target="_blank"
        class="
          favourite
          transition
          cursor-pointer
          group
          hover:text-white
          hover:bg-blue-400
          hover:border-blue-400
          w-1/2
          p-4
          border
          flex
          items-center
          justify-center
        "
      >
        <span class="play-toggle mx-2">
          <SvgIcon
            cls="group-hover:text-white fill-current w-5 h-5 text-gray-700 cursor-pointer "
            icon="download"
          />
        </span>
        <span class="font-bold mt-2">download</span>
      </a>
    </div>
  </div>
</template>
<script>
import SvgIcon from "./SvgIcon.vue";

export default {
  name: "song",
  props: ["song"],
  components: {
    SvgIcon,
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
  },
};
</script>
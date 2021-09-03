<template>
  <div class="audiolist">
    <div
      class="
        songs
        my-4
        grid grid-cols-1
        lg:grid-cols-3
        md:grid-cols-2
        sm:grid-cols-1
        xs:grid-cols-1
        text-center
        mx-auto
        px-2
        gap-4
      "
    >
      <Song v-for="song in $store.state.songs" :key="song.id" :song="song" />
    </div>
  </div>
</template>


<script>
import Song from "./Song.vue";
// import axios from "axios";
export default {
  name: "AudioList",
  components: {
    Song,
  },
  data() {
    return {};
  },
  mounted() {},
};
</script>
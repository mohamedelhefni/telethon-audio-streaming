<template>
  <div class="audiolist">
    <p v-if="$store.state.songs.length " class="text-gray text-left my-3 ml-3">Audio Files: <b>{{ $store.state.pagination.total }}</b> , Pages:  <b> {{ $store.state.pagination.totalPages }} </b> </p>
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
    <div v-if="$store.state.endOfFiles" class="text-center text-gray">
      There were no more files 
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
<template>
  <div class="container mx-auto pb-40">
    <div class="header w-full max-w-3xl mx-auto">
      <h1 class="text-6xl mt-4 mb-5 font-bold text-center text-gray-800">
        Telegram Audio Streaming
      </h1>
      <SearchForm />
    </div>
    <div
      v-if="
        !$store.state.error &&
        !$store.state.loading &&
        $store.state.songs.length == 0
      "
      class="info text-lg mt-10 p-2 max-w-3xl mx-auto text-left leading-8"
    >
      Telegram audio streaming is a service that allows you to get telegram
      channel audio files and listen to it or download it by putting the
      username in the form above for example: <br />
      <b>Arabic: </b> audiobooking1 or @audiobooking1, drsulafa, all_podcast,
      Arabicpodcasts <br />
      <b>English: </b> podcast_english_listening, amazonebook, ingliztiliuzz,
      English_podcasts
    </div>
    <div
      v-if="$store.state.error"
      class="font-bold my-2 mt-10 text-gray-700 text-xl"
    >
      the username is incorrect please try again with valid telegram channel
      username.
    </div>
    <Loading v-if="$store.state.loading" />
    <SongsList v-if="!$store.state.loading && !$store.state.error" />
    <SongPlayer
      v-if="$store.state.currentUrl.length > 0"
      :song="$store.state.currentSong"
    />
  </div>
</template>

<script>
import SongsList from "./components/SongsList.vue";
import SearchForm from "./components/SearchForm.vue";
import SongPlayer from "./components/SongPlayer.vue";
import Loading from "./components/Loading.vue";

export default {
  name: "App",
  components: {
    SongsList,
    SearchForm,
    SongPlayer,
    Loading,
  },
  methods: {},
};
</script>

<style>
#app {
  font-family: "Roboto", Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

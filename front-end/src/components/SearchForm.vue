<template>
  <div class="search-form mx-auto">
    <form
      @submit.prevent="getChannelSongs"
      class="flex items-center justify-around"
    >
      <input
        type="text"
        v-model="channel"
        name="channel"
        class="
          shadow
          appearance-none
          border
          font-bold
          text-large
          focus:border-gray-500
          rounded
          w-full
          py-2
          px-3
          mx-3
          text-gray-700
          leading-tight
          focus:outline-none
          focus:shadow-outline
        "
        placeholder="Channel Username ...."
      />
      <button @click="getChannelSongs" class="search bg-gray-500 p-2 rounded">
        <SvgIcon cls="fill-current text-white cursor-pointer " icon="search" />
      </button>
    </form>
  </div>
</template>

<script>
import SvgIcon from "./SvgIcon.vue";

export default {
  name: "Search Form",
  components: {
    SvgIcon,
  },
  data() {
    return {
      channel: "",
    };
  },
  methods: {
    getChannelSongs() {
      if (this.channel.length > 3) {
        this.$store.dispatch("changeSongs", this.channel);
      }
    },
  },
};
</script>
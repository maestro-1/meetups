<template>
  <v-alert type="info" dismissible @input="onClose" :value="true">
    {{ text }}
  </v-alert>
</template>

<script>
export default {
  props: ["text"],

  setup(props, { emit }) {
    const onClose = () => {
      emit("dismissed");
    };
    return { onClose };
  }
};
</script>

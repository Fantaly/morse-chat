<template>
    <div id="InputLabel">
        <VLabel>{{ label }}</VLabel>
        <slot></slot>
    </div>
</template>

<script setup lang="ts">
import VLabel from '../label/VLabel.vue';

interface props{
    label: string
}

const props = withDefaults(defineProps<props>(), {

})

</script>

<style scoped>
#InputLabel{
    display: flex;
    flex-direction: column;
    gap: 8px;
}
</style>
<template>
    <input type="text" class="input border-0 shadow" :class="fullwidth && 'is-full'" :placeholder="placeholder"
        v-model="modelValue">
</template>

<script setup lang="ts">
const modelValue = defineModel()

interface props {
    fullwidth: boolean,
    placeholder: string
}

const props = withDefaults(defineProps<props>(), {
    fullwidth: false,
    placeholder: 'Placeholder...'
})

</script>

<style scoped lang="scss">
.input {
    box-sizing: border-box;
    -moz-box-sizing: border-box;
    -webkit-box-sizing: border-box;
    background-color: transparent;
    border: none;
    padding: 14px 16px;
    border-radius: 8px;
    font-size: 14px;
    line-height: 20px;
}

.border-0 {
    // border: 1px solid var(--black-100);    
}

.shadow {
    transition: all 0.25s ease;
    box-shadow: 0 0 0 1px var(--black-50);

    &:hover,
    &:focus {
        transition: all 0.25s ease;
        box-shadow: 0 0 0 2px var(--black-100);
    }

}

.size {}

.color {}

.is-full {
    width: 100%;
}
</style>
<template>
    <div id="login">
        <div class="login">
            <div class="welcome mb-48">
                <h1 class="semibold mb-12">
                    Welcome Back
                </h1>

                <p class="regular">Enter your email and password to access your account</p>

            </div>
            <div class="mb-48">
                <VInputLabel label="Email" class="mb-16">
                    <VInput v-model="textTest"></VInput>
                </VInputLabel>

                <VInputLabel label="Password">
                    <VInput></VInput>
                </VInputLabel>
            </div>
            <VButton :size="'medium'" :color="'default'" :fullwidth="true">Sign in
                <template v-slot:right>
                    <VIconSvg icon="arrow-right"></VIconSvg>
                </template>
            </VButton>
            <h2>{{ textTest }}</h2>
        </div>
    </div>
</template>

<script setup lang="ts">

import VButton from '@/components/base/button/VButton.vue';
import VIconSvg from '@/components/base/icon/VIconSvg.vue';
import VLabel from '@/components/base/label/VLabel.vue';
import VInput from '@/components/base/input/VInput.vue'
import VInputLabel from '@/components/base/input/VInputLabel.vue';
import { ref } from 'vue';

const textTest = ref('');
</script>

<style scoped>
#login {
    display: flex;
    flex-direction: column;
    gap: 40px;
    align-items: center;
    padding: 32px 32px;
}

h1 {
    line-height: normal;
    font-size: 48px;
    /* font-family: 'Poppins', sans-serif; */
}

.welcome {
    text-align: center;
}

p {
    font-size: 14px;
    font-family: 'Poppins', sans-serif;
}
</style>
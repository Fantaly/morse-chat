<template>
    <div id="login">
        <form class="login" @submit.prevent="handleLogin" >
            <div class="welcome mb-48">
                <h1 class="regular mb-12">
                    Welcome Back
                </h1>
                <p class="regular">Enter your email and password to access your account</p>
            </div>
            <div class="mb-48">
                <VInputLabel label="Email" class="mb-16" forId="email" aria-required>
                    <VInput v-model="email" id="email" placeholder="Enter your email" aria-required="true"></VInput>
                </VInputLabel>

                <VInputLabel label="Password" forId="password" aria-required>
                    <VInput v-model="password" inputType="password" id="password" placeholder="Enter your password" aria-required="true" required></VInput>
                </VInputLabel>

            </div>
            <VButton class="mb-32" size="medium" :color="loading ? 'loading' : 'default'" :fullwidth="true" :loading="loading" @click="loading = true">Sign in
                <template v-slot:right>
                    <VIconSvg icon="arrow-right"></VIconSvg>
                </template>
            </VButton>
        </form>
    </div>
</template>

<script setup lang="ts">

import VButton from '@/components/base/button/VButton.vue';
import VIconSvg from '@/components/base/icon/VIconSvg.vue';
import VInput from '@/components/base/input/VInput.vue'
import VInputLabel from '@/components/base/input/VInputLabel.vue';
import { useAuthStore } from '@/stores/auth';
import { watch } from 'vue';
import { ref } from 'vue';

const login  = useAuthStore();
const email = ref('');
const password = ref('');

const handleLogin = () => {
    login.login({
        username: email.value,
        password: password.value
    });
};

const loading = ref(false);

watch(loading, (newVal) => {
    console.log(newVal);
});

const textTest = ref('');
</script>

<style scoped>

#login {
    display: flex;
    flex-direction: column;
    gap: 40px;
    align-items: center;
    padding: 32px 32px;
    height: 100%;
    justify-content: center;
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
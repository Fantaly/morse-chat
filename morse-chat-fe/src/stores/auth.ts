import type { AuthInfo, LoginInfo } from '@/interfaces/components.interfaces';
import router from '@/router';
import axios from 'axios';
import { defineStore } from 'pinia'

interface State {
  user: string | null;
  token: string | null;
}

export const useAuthStore = defineStore('auth', {
  state: (): State => ({
    user: '',
    token: '',
  }),
  getters: {
    isAuthenticated: (state) => !!state.user,
  },
  actions: {
    async login(userInfo: LoginInfo) {
      try {
          const formData = new URLSearchParams();
          formData.append('username', userInfo.username); // Assuming userInfo.email is the user's email
          formData.append('password', userInfo.password);
  
          const response = await axios.post(
              'http://localhost:8000/token/',
              formData,
              {
                  headers: {
                      'Content-Type': 'application/x-www-form-urlencoded'
                  }
              }
          );
  
          this.user = userInfo.username; // Ensure this line correctly sets the user information based on your application's needs
  
          localStorage.setItem('token', response.data.access_token); // Make sure to use 'access_token' as per your backend response
          router.push({ name: 'main' });
      } catch (error) {
          console.error(error);
      }
  },
  
    logout() {
      this.user = null;
      this.token = null;
      // Remove token from localStorage or cookies
    },
  },
})
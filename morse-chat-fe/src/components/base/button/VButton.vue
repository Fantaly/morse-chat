<template>
    <button class="btn" :class="[
        `is-${size}`,
        color && `btn-${color}`,
        fullwidth && 'w-100',
    ]">
        <slot name="left"></slot>
        <div class="content">
        
          <slot v-if="!loading"></slot>
          <LoadingButton v-else/>
        
        </div>
        <slot name="right"></slot>
    </button>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue';
import LoadingButton from '../loading/LoadingButton.vue';

type VButtonSize = "xs" | "small" | "medium" | "large";

export type VButtonColor =
    | "error"
    | "primary"
    | "primary-100"
    | "secondary"
    | "secondary-light"
    | "success"
    | "warning"
    | "default"
    | "loading"

interface VButtonProps {
    action?: string;
    active?: boolean;
    color?: VButtonColor | undefined;
    disabled?: boolean;
    fullwidth?: boolean;
    icon?: string | null;
    notification?: boolean;
    size?: VButtonSize;
    loading?: boolean;
}

const props = withDefaults(defineProps<VButtonProps>(), {
    action: "",
    active: false,
    color: "success",
    disabled: false,
    fullwidth: false,
    icon: null,
    notification: false,
    size: "large",
    loading: false,
});

// const iconDimension = computed<number>(() => {
//   return props.iconSize ? props.iconSize : props.size === "xs" ? 16 : 24;
// });

</script>

<style lang="scss" scoped>
.btn-loading{
  border: 1px solid black;
}
.btn {
    .content{
      height: 20px;
      display: flex;
      justify-content: center;
      align-items: center;
    }

    transition: all 0.2s ease;
    background: #23A6F0;
    color: white;
    border: none;
    cursor: pointer;
    font-family: 'Inter';
    border-radius: 8px;
    background: var(--Brand-600, #121212);
    box-shadow: 0px 1px 2px 0px rgba(16, 24, 40, 0.05);

    &.is-xs {
        @include text-style(600, 12, 1.1);
        padding: 1px 7px;

        &.no-action {
            padding: 3px;
            border-radius: 5px;
        }
    }

    &.is-small {
        @include text-style(600, 14, 1.1);
        padding: 4px 8px;

        &.no-action {
            padding: 4px;
            border-radius: 7px;
        }
    }

    &.is-medium {
        @include text-style(500, 16, 0.3);
        padding: 12px 16px;

        &.no-action {
            padding: 7px;
        }
    }

    &.is-large {
        @include text-style(700, 18, 0.3);
        padding: 11px 15px;

        &.no-action {
            padding: 11px;
            border-radius: 11px;
        }
    }

    /* ==========================================================================
    Default
  ========================================================================== */

  @include btn-style(".btn-default", default, var(--grey-100), var(--primary-p));
  @include btn-style(".btn-default", hover, var(--primary-p), var(--grey-100));
  @include btn-style(".btn-default", active, var(--accent-300), var(--accent-100));
  @include btn-style(".btn-default", disabled, base, var(--grey-500));

  /* ==========================================================================
    Accent
  ========================================================================== */


  /* ==========================================================================
    Accent 600
  ========================================================================== */


  /* ==========================================================================
    Blue-gray
  ========================================================================== */


  /* ==========================================================================
    Secondary
  ========================================================================== */


  /* ==========================================================================
    Secondary light
  ========================================================================== */


  /* ==========================================================================
    Primary
  ========================================================================== */


  /* ==========================================================================
    Primary 100
  ========================================================================== */


  /* ==========================================================================
    Error
  ========================================================================== */


  /* ==========================================================================
    Error alt
  ========================================================================== */


  /* ==========================================================================
    Success
  ========================================================================== */


  /* ==========================================================================
    Warning
  ========================================================================== */

  /* ==========================================================================
    Loading
  ========================================================================== */
  @include btn-style(".btn-loading", default, var(--black-p), var(---grey-100));

}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.3s;
}
</style>
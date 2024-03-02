<template>
    <button class="btn" :class="[
        `is-${size}`,
        color && `btn-${color}`,
        fullwidth && 'w-100',
    ]">
        <slot name="left"></slot>
        <slot></slot>
        <slot name="right"></slot>
    </button>
</template>

<script setup lang="ts">
import { computed } from 'vue';

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

interface VButtonProps {
    action?: string;
    active?: boolean;
    color?: VButtonColor | undefined;
    disabled?: boolean;
    fullwidth?: boolean;
    icon?: string | null;
    notification?: boolean;
    size?: VButtonSize;
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
});

// const iconDimension = computed<number>(() => {
//   return props.iconSize ? props.iconSize : props.size === "xs" ? 16 : 24;
// });

</script>

<style lang="scss" scoped>
.btn {
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
  @include btn-style(".btn-default", active, var(--accent-700), var(--accent-300));
  @include btn-style(".btn-default", disabled, base, var(--grey-500));

  /* ==========================================================================
    Accent
  ========================================================================== */

  @include btn-style(".btn-accent", default, var(--white-90), var(--accent-p));
  @include btn-style(".btn-accent", hover, base, var(--accent-400));
  @include btn-style(".btn-accent", active, base, var(--accent-700));
  @include btn-style(".btn-accent", disabled);

  /* ==========================================================================
    Accent 600
  ========================================================================== */

  @include btn-style(".btn-accent-600", default, var(--white-90), var(--accent-600));
  @include btn-style(".btn-accent-600", hover, base, var(--accent-400));
  @include btn-style(".btn-accent-600", active, base, var(--accent-700));
  @include btn-style(".btn-accent-600", disabled);

  /* ==========================================================================
    Blue-gray
  ========================================================================== */

  @include btn-style(".btn-blue-grey", default, var(--white-90), var(--blue-grey));
  @include btn-style(".btn-blue-grey", hover, base, var(--blue-grey-light));
  @include btn-style(".btn-blue-grey", active, base, var(--blue-grey-dark));
  @include btn-style(".btn-blue-grey", disabled, base, var(--blue-grey-dark));

  /* ==========================================================================
    Secondary
  ========================================================================== */

  @include btn-style(".btn-secondary", default, var(--primary-p), transparent);
  @include btn-style(".btn-secondary", hover, var(--accent-p), var(--accent-100));
  @include btn-style(".btn-secondary", active, var(--accent-p), var(--accent-200));
  @include btn-style(".btn-secondary", disabled);

  /* ==========================================================================
    Secondary light
  ========================================================================== */

  @include btn-style(".btn-secondary-light", default, var(--white-100), transparent);
  @include btn-style(".btn-secondary-light", hover, var(--accent-p), var(--accent-100));
  @include btn-style(".btn-secondary-light", active, var(--accent-p), var(--accent-200));
  @include btn-style(".btn-secondary-light", disabled, var(--primary-p), transparent);

  /* ==========================================================================
    Primary
  ========================================================================== */

  @include btn-style(".btn-primary", default, var(--white-90), var(--primary-p));
  @include btn-style(".btn-primary", hover, base, var(--primary-200));
  @include btn-style(".btn-primary", active, base, var(--primary-500));
  @include btn-style(".btn-primary", disabled);

  /* ==========================================================================
    Primary 100
  ========================================================================== */

  @include btn-style(".btn-primary-100", default, var(--white-90), var(--primary-100));
  @include btn-style(".btn-primary-100", hover, base, var(--primary-75));
  @include btn-style(".btn-primary-100", active, base, var(--primary-200));
  @include btn-style(".btn-primary-100", disabled, base, var(--primary-200));

  /* ==========================================================================
    Error
  ========================================================================== */

  @include btn-style(".btn-error", default, var(--white-90), var(--error-p));
  @include btn-style(".btn-error", hover, base, var(--error-300));
  @include btn-style(".btn-error", active, base, var(--error-500));
  @include btn-style(".btn-error", disabled);
  @include btn-style(".btn-error.no-action", default, var(--primary-p), var(--grey-300));
  @include btn-style(".btn-error.no-action", hover, var(--error-p), var(--error-100));
  @include btn-style(".btn-error.no-action", active, var(--error-500), var(--error-200));
  @include btn-style(".btn-error.no-action", disabled, var(--primary-300), var(--grey-500));

  /* ==========================================================================
    Error alt
  ========================================================================== */

  @include btn-style(".btn-error-alt", default, var(--error-p), transparent);
  @include btn-style(".btn-error-alt", default, base, var(--grey-300), "large");
  @include btn-style(".btn-error-alt", hover, base, var(--error-100));
  @include btn-style(".btn-error-alt", active, var(--error-500), var(--error-200));
  @include btn-style(".btn-error-alt", disabled, base, var(--grey-400));

  /* ==========================================================================
    Success
  ========================================================================== */

  @include btn-style(".btn-success", default, var(--primary-p), var(--grey-300));
  @include btn-style(".btn-success", hover, var(--success-500), var(--success-100));
  @include btn-style(".btn-success", active, var(--success-500), var(--success-200));
  @include btn-style(".btn-success", disabled, var(--primary-300), var(--grey-500));

  /* ==========================================================================
    Warning
  ========================================================================== */

  @include btn-style(".btn-warning", default, var(--primary-p), var(--grey-300));
  @include btn-style(".btn-warning", hover, var(--warning-p), var(--warning-100));
  @include btn-style(".btn-warning", active, var(--warning-500), var(--warning-200));
  @include btn-style(".btn-warning", disabled, var(--primary-300), var(--grey-500));
}

</style>
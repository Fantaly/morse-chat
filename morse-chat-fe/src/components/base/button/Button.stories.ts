import type { Meta, StoryObj } from '@storybook/vue3';

import VButton from './VButton.vue';

const meta: Meta<typeof VButton> = {
    component: VButton,
    argTypes: {
        color: {
            control: 'select',
            options: [
                "accent", "accent-600", "blue-grey", "error", "error-alt", 
                "primary", "primary-100", "secondary", "secondary-light", 
                "success", "warning", "klarna", "stripe", "facebook", 
                "instagram", "linkedin"
            ],
        },
        size: {
            control: 'select',
            options: ['xs', 'small', 'medium', 'large'],
        },
        disabled: {
            control: 'boolean',
        }
    }
};

export default meta;

type Story = StoryObj<typeof VButton>;

export const Primary: Story = {
    render: () => ({
        components: { VButton },
        template: '<VButton v-bind="args" label="Button">Button example</VButton>',
    }),
};
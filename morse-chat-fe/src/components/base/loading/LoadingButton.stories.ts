import ButtonLoader from './LoadingButton.vue'; // Adjust the path as necessary

export default {
  title: 'Components/ButtonLoader',
  component: ButtonLoader,
};

const Template = (args, { argTypes }) => ({
  components: { ButtonLoader },
  props: Object.keys(argTypes),
  template: '<button-loader />',
});

export const Default = Template.bind({});

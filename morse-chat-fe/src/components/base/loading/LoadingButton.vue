<template>
    <div class="button-loader">
        <div></div>
        <div></div>
        <div></div>
    </div>
</template>

<style scoped>
.button-loader>div {
    width: .8rem;
    height: .8rem;
    background-color: rgb(0, 0, 0);
    border-radius: 50%;
    animation: 1.2s infinite ease-in-out load;
}

.button-loader div:nth-child(1) {
    animation-delay: -0.32s;
}

.button-loader div:nth-child(2) {
    animation-delay: -0.16s;
}

.button-loader{
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 1px;
    height: 7px;

}

@keyframes load {

    0%,
    80%,
    100% {
        transform: scale(0);
    }

    40% {
        transform: scale(1);
    }
}
</style>
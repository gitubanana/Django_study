const elems = document.getElementsByClassName('splide')
for (let i = 0; i < elems.length; ++i)
{
    var splide = new Splide(elems[i], {
        type  : 'fade',
        rewind: true,
    } );

    splide.mount();
}
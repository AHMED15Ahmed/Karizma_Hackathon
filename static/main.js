function searchRecipes() {
    const searchInput = document.getElementById('searchInput').value.toLowerCase();
    const recipeList = document.getElementById('recipeList');
    const recipes = recipeList.getElementsByTagName('li');

    for (let i = 0; i < recipes.length; i++) {
        const recipeName = recipes[i].getElementsByTagName('h3')[0].innerText.toLowerCase();

        if (recipeName.includes(searchInput)) {
            recipes[i].style.display = 'block';
        } else {
            recipes[i].style.display = 'none';
        }
    }
}

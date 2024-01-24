document.addEventListener('DOMContentLoaded', function() {
    var checkExist = setInterval(function() {
        var divider = document.querySelector('.wh-header__divider');
        if (divider) {
            clearInterval(checkExist);

            // Create a container for the switch engine section
            var switchContainer = document.createElement('div');
            switchContainer.style.textAlign = 'right'; // Right align the content
            switchContainer.style.paddingRight = '20px'; // Right padding

            // Create the "Switch Engine:" text
            var switchText = document.createElement('span');
            switchText.textContent = 'Switch Engine:';
            switchText.style.marginRight = '10px'; // Spacing

            // Create the Unreal link
            var unrealLink = document.createElement('a');
            unrealLink.href = '/unreal';
            unrealLink.textContent = 'Unreal';
            unrealLink.style.fontSize = '1em'; // Smaller font size
            unrealLink.style.color = 'grey'; // Grey color
            unrealLink.style.marginRight = '10px'; // Spacing

            // Create the Unreal text (not a link)
            var unityText = document.createElement('span');
            unityText.textContent = 'Unity';
            unityText.style.fontSize = '1.2em'; // Bigger font size

            // Append elements to the container
            switchContainer.appendChild(switchText);
            switchContainer.appendChild(unrealLink);
            switchContainer.appendChild(unityText);

            // Append the container to the divider
            divider.appendChild(switchContainer);
        }
    }, 100);
});

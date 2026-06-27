async function getSongs() {

    const response = await fetch(
        "http://127.0.0.1:8000/songs"
    )

    const songs = await response.json()

    const container =
        document.getElementById("songs-container")

    container.innerHTML = ""

    for (const song of songs) {
        container.innerHTML += `
            <div class='song-card'>
                <h3 class='song-title'>
                    ${song.title}
                </h3>

                <p class='song-artist'>
                    ${song.artist}
                </p>

                <div class='song-actions'>
                    <button>Editar</button>
                    <button class='song-delete' data-id='${song.id}'>Eliminar</button>
                </div>
            </div>
            `
    }

    const deleteButtons =
        document.querySelectorAll(".song-delete")

    for (const button of deleteButtons) {
        button.addEventListener("click", async () => {
            const songId = button.dataset.id

            await fetch(
                `http://127.0.0.1:8000/songs/${songId}`,
                {
                    method: "DELETE"
                }
            )

            getSongs()
        })
    }
}

getSongs()

const form = document.getElementById("song-form")

form.addEventListener("submit", async (event) => {
    event.preventDefault()

    const titleInput = document.getElementById("title")
    const artistInput = document.getElementById("artist")

    await fetch("http://127.0.0.1:8000/songs", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            title: titleInput.value,
            artist: artistInput.value
        })
    })

    titleInput.value = ""
    artistInput.value = ""

    getSongs()
})
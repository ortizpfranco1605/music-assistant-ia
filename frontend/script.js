let songs = []
let editingSongId = null

async function getSongs() {

    const response = await fetch(
        "http://127.0.0.1:8000/songs"
    )

    songs = await response.json()

    const container =
        document.getElementById("songs-container")

    container.innerHTML = ""

    for (const song of songs) {

        container.innerHTML += `
            <div class="song-card">

                <h3 class="song-title">
                    ${song.title}
                </h3>

                <p class="song-artist">
                    ${song.artist}
                </p>

                <div class="song-actions">
                    <button
                        class="song-edit"
                        data-id="${song.id}">
                        Editar
                    </button>

                    <button
                        class="song-delete"
                        data-id="${song.id}">
                        Eliminar
                    </button>
                </div>

            </div>
        `
    }

    // BOTONES ELIMINAR

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

    // BOTONES EDITAR

    const editButtons =
        document.querySelectorAll(".song-edit")

    for (const button of editButtons) {

        button.addEventListener("click", () => {

            const songId = Number(button.dataset.id)

            const song =
                songs.find(song => song.id === songId)

            const titleInput =
                document.getElementById("title")

            const artistInput =
                document.getElementById("artist")

            titleInput.value = song.title
            artistInput.value = song.artist

            titleInput.select()

            editingSongId = song.id
            submitButton.textContent = "Guardar cambios"

        })

    }

}

const form = document.getElementById("song-form")
const submitButton = document.getElementById("submit-button")

form.addEventListener("submit", async (event) => {

    event.preventDefault()

    const titleInput =
        document.getElementById("title")

    const artistInput =
        document.getElementById("artist")

    if (editingSongId === null) {

        // POST

        await fetch(
            "http://127.0.0.1:8000/songs",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    title: titleInput.value,
                    artist: artistInput.value
                })
            }
        )

    } else {

        // PUT

        await fetch(
            `http://127.0.0.1:8000/songs/${editingSongId}`,
            {
                method: "PUT",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    title: titleInput.value,
                    artist: artistInput.value
                })
            }
        )

        editingSongId = null

        submitButton.textContent= "Agregar"

    }

    titleInput.value = ""
    artistInput.value = ""

    getSongs()

})

getSongs()
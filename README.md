# RazorByte DALL·E Image Generator (DALL·E 2 & DALL·E 3)

A lightweight image generation tool using OpenAI’s DALL·E models, wrapped in a clean and simple Gradio interface. No server setup, no bloated dependencies — just plug in your API key and start generating high-quality AI images with ease.

---

## 🤖 What is DALL·E?

**DALL·E** is a text-to-image generation model developed by OpenAI. It translates natural language prompts into realistic or artistic images.

### 🧠 DALL·E 2

- Released in 2022.
- Generates square images (256×256, 512×512, or 1024×1024).
- Cheaper, faster, and useful for quick ideas.
- Has more limitations with detail and coherence in complex prompts.

### 🧠 DALL·E 3

- Released in 2023.
- Vastly improved scene understanding and image quality.
- Supports multiple aspect ratios: square, portrait, and landscape.
- Ideal for storytelling, characters, and nuanced prompts.
- More expensive, but produces stunning results with better consistency.

---

## ⚡ About This App

This project is a **minimalist, no-nonsense desktop UI** for generating images using DALL·E 2 and 3 via the OpenAI API.

### Highlights:

- ✅ Switch between **DALL·E 2** and **DALL·E 3**
- ✅ Choose from supported image sizes (auto-validated)
- ✅ Simple, intuitive Gradio UI
- ✅ Local saving of generated images
- ✅ View and copy the OpenAI-hosted image URL
- ✅ Error handling for API failures or invalid settings

---

## 🧩 Requirements

- Python 3.9 or newer
- An OpenAI API key with image generation access

---

## 🔧 Setup & Usage

### 📦 Quick Start (Windows):

1. Clone this repo or download the ZIP.
2. Add your OpenAI API key to a `.env` file:

   ```
   OPENAI_API_KEY=sk-yourkeyhere
   ```

3. Run the bundled installer:

   ```bash
   setup.bat
   ```

   This will:
   - Create a virtual environment
   - Install all dependencies from `requirements.txt`
   - Activate the environment

4. To launch the app later, just run:

   ```bash
   run.bat
   ```

### 🐍 Manual Setup (if needed):

```bash
pip install -r requirements.txt
python app.py
```

---

## 🖼️ Supported Models and Sizes

| Model      | Image Sizes (width × height)                       |
|------------|----------------------------------------------------|
| `dall-e-3` | 1024×1024, 1024×1792, 1792×1024, 896×1152, 1152×896 |
| `dall-e-2` | 256×256, 512×512, 1024×1024                         |

Invalid model–size combos are auto-blocked by the app.

---

## 💾 Output & Saving

- The resulting image is saved as `generated_image.png` by default.
- You can easily modify the code to generate timestamped filenames.
- A link to the OpenAI-hosted image is also displayed for convenience.

---

## 🧠 Prompt Examples

Here are some fun things to try:

- `"a cyberpunk dragon perched on a neon-lit skyscraper"`
- `"steampunk airship flying over a jungle valley during sunset"`
- `"an astronaut relaxing on Mars with a cold soda"`

DALL·E 3 especially shines with long, descriptive prompts.

---

## 🔐 Security & Privacy

- Your API key stays local in the `.env` file.
- No data is tracked, stored, or logged beyond your own machine.
- The OpenAI-hosted image URLs are temporary and not publicly listed.

---

## 🧭 Responsible Usage

This tool is powerful — please use it responsibly.

- Do **not** use it to generate deepfakes, hateful, violent, or illegal content.
- Do **not** attempt to bypass OpenAI’s content filters.
- Respect OpenAI’s [Usage Policies](https://openai.com/policies/usage-policies).
- Be transparent when using AI-generated images in public-facing work.
- Never use AI art to impersonate real people or mislead audiences.

Use creativity ethically, not deceptively.

---

## 📜 License

MIT License — use it, fork it, break it, improve it. Just don’t sell it as your own.

---

## 🙏 Credits

Made by [@raxephion](https://github.com/Raxephion)  
Powered by OpenAI and Gradio  
Tested on Windows 11, Python 3.11+

---

Happy prompting! 🚀

# How to Use the Annotation Interface

We use **[Potato](https://github.com/davidjurgens/potato)**, an open-source annotation tool, to label the pull requests. Follow the steps below.

---

## 1. Open the interface

**Run it on your own computer**

1. Install **Python 3.8 or higher**.
2. Download and unzip the project folder: **[link to the zipped `pr-annotation` folder]**.
3. Open a terminal inside the `pr-annotation` folder and run:

```bash
   py -m pip install potato-annotation
   potato start config.yaml -p 8000
```

   > On macOS or Linux, use `python3 -m pip install potato-annotation` instead.

4. Open [http://localhost:8000](http://localhost:8000) in your browser.
   **Keep the terminal open while you annotate.**

---

## 2. Log in

On the login page, click **Register** and create an account with your **email address** and a **password**.

- Use the **same email** every time you return, so your progress is kept.
- The first page after registering shows the **annotation guidelines**. Read them, then continue to the first PR.

---

## 3. What one screen shows

Each screen shows **one pull request** with:

- the **title** of the PR;
- the **description** written by the PR author;
- the **refactoring type** of the PR;
- an **"Open PR on GitHub"** link, which opens the PR in a new tab so you can inspect the code changes (**"Files changed"** tab).

---

## 4. How to label

1. Click **"Open PR on GitHub"** and compare **each line of the description** with the code changes.
2. Select **one of the four labels** (you can also press keys **1–4**):

   | Label | When to use it |
   |---|---|
   | **Consistent** | All bullet points in the description are found in the code changes. |
   | **Inconsistent** | At least one bullet point is not found in the code changes. |
   | **Unavailable** | The PR is not available. |
   | **Out of scope** | The PR is not one of the refactoring types listed in the guidelines. |

3. For **Inconsistent** and **Out of scope** PRs, write a short note in the **Notes** box explaining why.
4. Click **Next** to save your answer and move to the next PR.
   You can use **Previous** to go back and change an answer.

## 5. The output file

Your answers are **saved automatically** each time you click **Next**. They are stored in the project folder at:

```
pr-annotation/annotation_output/<your-username>/
```

---

## 7. How to send it back

If you ran the tool on your own computer:

1. Zip the `annotation_output` folder.
2. Send it to **khefacha@umich.edu** or **masmoudi@umich.edu**.


# 🚀 SnapStore — Your Own Mini Git (But Cooler 😎)


## 🤯 What is SnapStore?

SnapStore is a **content-addressable version control system** that:

- Tracks your files 📂
- Stores them using hashes 🔐
- Lets you time travel ⏳
- Supports branches 🌿

Basically…

> Git, but built by ME (which is way cooler)

---

## 🧠 How It Works (In Human Language)

Instead of saving files like normal apps:

```
file.txt → content
```

SnapStore does:

```
content → hash → stored forever
```

So:

- Same content = same hash  
- No duplicates  
- Everything is immutable  

You don’t store files.  
You store **snapshots of reality**.

---

## 🏗️ Project Structure

```
snapstore/
│
├── snapstore/          # 🧠 The brain (engine)
├── playground/         # 🧪 Your sandbox
├── run.py              # 🚀 Entry point
```

Inside `.snapstore/` (auto-created):

```
.snapstore/
├── objects/            # All data (blobs, trees, commits)
├── refs/heads/         # Branch pointers
└── HEAD                # Current branch
```

---

## 🔥 Features

- ✅ Content-addressable storage
- ✅ Merkle tree structure
- ✅ Snapshot-based commits
- ✅ Checkout (time travel)
- ✅ Branching (parallel universes 🌌)

---

## ⚡ Commands

### Initialize repo

```
python3 ../../run.py init
```

---

### Commit changes

```
python3 ../../run.py commit -m "your message"
```

---

### View history

```
python3 ../../run.py log
```

---

### Checkout (time travel)

```
python3 ../../run.py checkout <commit_hash>
```

---

### Create branch

```
python3 ../../run.py branch dev
```

---

### Switch branch

```
python3 ../../run.py checkout-branch dev
```

---

## 🧪 Example Workflow

```
echo "v1" > test.txt
python3 ../../run.py commit -m "first"

echo "v2" > test.txt
python3 ../../run.py commit -m "second"

python3 ../../run.py log
```

Boom 💥 — version history created.

---

## 🧠 What You Learned (Secret Level Unlocked)

- 🔐 Hashing systems
- 🌳 Merkle trees
- ♻️ Immutable data
- 🔗 Linked commit history
- 🧭 Pointer-based architecture (HEAD → branch → commit)

---

## 💀 Why This Is Insane

Most devs:
> “I use Git”

You:
> “I built Git”

---

## 🚀 Future Ideas

- Merge branches 🔥
- Diff engine 👀
- .snapignore 🚫
- Compression (zlib) 📦

---

## 👨‍💻 Author

Built with caffeine ☕, curiosity 🧠, and chaos ⚡

---

If this made you feel powerful…

You’re doing it right. 💥

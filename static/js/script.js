/* ═══════════════════════════════════════
   MAGIC MOVIES — Global JS
═══════════════════════════════════════ */

// ─ Live Search ───────────────────────────────────────────────────
const searchInput = document.getElementById('nav-search');
const dropdown    = document.getElementById('search-dropdown');

if (searchInput && dropdown) {
  let debounceTimer;

  searchInput.addEventListener('input', () => {
    clearTimeout(debounceTimer);
    const q = searchInput.value.trim();
    if (!q) { dropdown.classList.remove('open'); return; }
    debounceTimer = setTimeout(() => fetchSearch(q), 280);
  });

  searchInput.addEventListener('keydown', e => {
    if (e.key === 'Escape') { dropdown.classList.remove('open'); searchInput.blur(); }
  });

  document.addEventListener('click', e => {
    if (!searchInput.contains(e.target) && !dropdown.contains(e.target)) {
      dropdown.classList.remove('open');
    }
  });

  async function fetchSearch(q) {
    try {
      const res  = await fetch(`/search?q=${encodeURIComponent(q)}`);
      const data = await res.json();
      renderDropdown(data, q);
    } catch(e) { /* fail silently */ }
  }

  function renderDropdown(results, q) {
    if (!results.length) {
      dropdown.innerHTML = `<div class="search-no-result">🔍 No movies found for "<strong>${q}</strong>"</div>`;
      dropdown.classList.add('open');
      return;
    }
    dropdown.innerHTML = results.map(m => `
      <a class="search-item" href="/movie/${m.id}">
        <div class="s-poster" style="overflow:hidden;border-radius:6px;padding:0;background:${m.poster_color}22;">
          <img src="/static/images/${m.poster_key}.svg" alt="${m.title}"
               style="width:36px;height:50px;object-fit:cover;display:block;">
        </div>
        <div class="s-info">
          <div class="s-title">${highlight(m.title, q)}</div>
          <div class="s-meta">${m.genre} · ${m.language}</div>
        </div>
        <div class="s-rating">⭐ ${m.rating}</div>
      </a>
    `).join('');
    dropdown.classList.add('open');
  }

  function highlight(text, q) {
    const re = new RegExp(`(${q.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')})`, 'gi');
    return text.replace(re, '<mark style="background:rgba(227,28,35,.25);color:inherit;border-radius:3px;padding:0 2px;">$1</mark>');
  }
}

// ─ Filter chips ──────────────────────────────────────────────────
document.querySelectorAll('.filter-chip').forEach(chip => {
  chip.addEventListener('click', () => {
    document.querySelectorAll('.filter-chip').forEach(c => c.classList.remove('active'));
    chip.classList.add('active');
  });
});

// ─ Date chips ────────────────────────────────────────────────────
document.querySelectorAll('.date-chip').forEach(chip => {
  chip.addEventListener('click', () => {
    document.querySelectorAll('.date-chip').forEach(c => c.classList.remove('sel'));
    chip.classList.add('sel');
    updateSummary();
  });
});

// ─ Time buttons ──────────────────────────────────────────────────
document.querySelectorAll('.time-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.time-btn').forEach(b => b.classList.remove('sel'));
    btn.classList.add('sel');
    updateSummary();
  });
});

// ─ Seat selection ────────────────────────────────────────────────
const MAX_SEATS = 8;
let selectedSeats = [];

document.querySelectorAll('.seat:not(.na)').forEach(seat => {
  seat.addEventListener('click', () => {
    const id = seat.dataset.id;
    if (seat.classList.contains('sel')) {
      seat.classList.remove('sel');
      const cls = seat.dataset.cls || '';
      seat.classList.add(cls);
      selectedSeats = selectedSeats.filter(s => s !== id);
    } else {
      if (selectedSeats.length >= MAX_SEATS) {
        showToast(`Max ${MAX_SEATS} seats per booking`); return;
      }
      const cls = seat.classList[1]; // save original class
      seat.dataset.cls = cls;
      seat.classList.remove(cls);
      seat.classList.add('sel');
      selectedSeats.push(id);
    }
    updateSummary();
  });
});

// ─ Payment method selection ──────────────────────────────────────
document.querySelectorAll('.pay-method-card').forEach(card => {
  card.addEventListener('click', () => {
    document.querySelectorAll('.pay-method-card').forEach(c => {
      c.classList.remove('sel');
      const r = c.querySelector('.pay-radio');
      if (r) { r.classList.remove('on'); r.innerHTML = ''; }
    });
    card.classList.add('sel');
    const radio = card.querySelector('.pay-radio');
    if (radio) radio.classList.add('on');

    const method = card.dataset.method;
    const upiForm  = document.getElementById('upi-form');
    const cardForm = document.getElementById('card-form');
    if (upiForm)  upiForm.classList.toggle('hide', method !== 'upi');
    if (cardForm) cardForm.classList.toggle('show', method === 'debit' || method === 'credit');

    // update hidden input
    const mInput = document.getElementById('selected-method');
    if (mInput) mInput.value = card.querySelector('.pay-label')?.textContent || 'UPI';
  });
});

// ─ UPI apps ──────────────────────────────────────────────────────
document.querySelectorAll('.upi-app-card').forEach(app => {
  app.addEventListener('click', () => {
    document.querySelectorAll('.upi-app-card').forEach(a => a.classList.remove('sel'));
    app.classList.add('sel');
  });
});

// ─ PIN auto-advance ──────────────────────────────────────────────
const pinBoxes = document.querySelectorAll('.pin-box');
pinBoxes.forEach((box, i) => {
  box.addEventListener('input', () => {
    box.value = box.value.replace(/\D/g,'').slice(0,1);
    if (box.value && pinBoxes[i+1]) pinBoxes[i+1].focus();
  });
  box.addEventListener('keydown', e => {
    if (e.key === 'Backspace' && !box.value && pinBoxes[i-1]) pinBoxes[i-1].focus();
  });
});

// ─ Summary updater ───────────────────────────────────────────────
function updateSummary() {
  const selDate = document.querySelector('.date-chip.sel');
  const selTime = document.querySelector('.time-btn.sel');

  const el = id => document.getElementById(id);
  if (el('sum-date') && selDate) {
    const d = selDate.querySelector('.dc-num')?.textContent || '';
    const m = selDate.querySelector('.dc-mon')?.textContent || '';
    const dy= selDate.querySelector('.dc-day')?.textContent || '';
    el('sum-date').textContent = `${dy}, ${d} ${m}`;
    const hi = document.getElementById('hidden-date');
    if (hi) hi.value = `${dy} ${d} ${m}`;
  }
  if (el('sum-time') && selTime) {
    el('sum-time').textContent = selTime.dataset.time || selTime.textContent.trim();
    const hi = document.getElementById('hidden-time');
    if (hi) hi.value = selTime.dataset.time || selTime.textContent.trim();
  }
  if (el('sum-seats')) {
    el('sum-seats').textContent = selectedSeats.length > 0 ? selectedSeats.join(', ') : '—';
    const hi = document.getElementById('hidden-seats');
    if (hi) hi.value = selectedSeats.join(', ');
  }
  // Price logic: seat category determines price
  const catEl = document.querySelector('.seat.sel');
  if (el('sum-total')) {
    const count = selectedSeats.length;
    if (count === 0) { el('sum-total').textContent = '—'; return; }
    // Detect price from which seats are selected
    let price = 200; // fallback
    const firstSeat = document.querySelector('.seat.sel');
    if (firstSeat) {
      const orig = firstSeat.dataset.cls || '';
      if (orig.includes('av-p'))      price = 450;
      else if (orig.includes('av-e')) price = 280;
      else                            price = 160;
    }
    const subtotal = count * price;
    const total = subtotal + 40;
    if (el('sum-subtotal'))  el('sum-subtotal').textContent  = `₹${subtotal}`;
    el('sum-total').textContent = `₹${total}`;
    const hi = document.getElementById('hidden-total');
    if (hi) hi.value = total;
    const hicat = document.getElementById('hidden-cat');
    if (hicat) {
      hicat.value = price === 450 ? 'Premium' : price === 280 ? 'Executive' : 'Normal';
    }
  }

  // Proceed button
  const proceedBtn = document.getElementById('proceed-btn');
  if (proceedBtn) {
    const ready = selectedSeats.length > 0 && selDate && selTime;
    proceedBtn.disabled = !ready;
    proceedBtn.style.opacity = ready ? '1' : '0.45';
    proceedBtn.style.pointerEvents = ready ? 'auto' : 'none';
  }
}

// ─ Pay button ────────────────────────────────────────────────────
const payBtn = document.getElementById('pay-now-btn');
if (payBtn) {
  payBtn.addEventListener('click', function() {
    const method = document.getElementById('selected-method')?.value || 'UPI';
    const isUpi  = !document.getElementById('upi-form')?.classList.contains('hide');

    if (isUpi) {
      const pins = [...document.querySelectorAll('.pin-box')];
      const pin  = pins.map(p => p.value).join('');
      if (pin.length < pins.length) {
        shakePins(); showToast('Enter your complete UPI PIN'); return;
      }
    }

    // Animate button
    payBtn.innerHTML = `<span style="display:inline-block;width:16px;height:16px;border:2.5px solid rgba(255,255,255,.3);border-top-color:#fff;border-radius:50%;animation:spin .7s linear infinite;"></span>&nbsp;Processing…`;
    payBtn.disabled = true;

    // Submit hidden form
    setTimeout(() => {
      document.getElementById('pay-form').submit();
    }, 1800);
  });
}

function shakePins() {
  const w = document.querySelector('.pin-boxes');
  if (!w) return;
  let n = 0;
  const t = setInterval(() => {
    w.style.transform = n%2===0 ? 'translateX(-6px)' : 'translateX(6px)';
    if (++n > 5) { clearInterval(t); w.style.transform='none'; }
  }, 55);
}

// ─ Download ticket ───────────────────────────────────────────────
window.downloadTicket = function() {
  const btn = document.getElementById('download-btn');
  if (!btn) return;
  const orig = btn.innerHTML;
  btn.innerHTML = `<span style="display:inline-block;width:15px;height:15px;border:2px solid rgba(255,255,255,.3);border-top-color:#fff;border-radius:50%;animation:spin .7s linear infinite;"></span>&nbsp;Preparing…`;
  btn.disabled = true;
  setTimeout(() => {
    window.print();
    btn.innerHTML = `<span class="download-icon">✅</span> Downloaded!`;
    setTimeout(() => { btn.innerHTML = orig; btn.disabled = false; }, 2500);
  }, 1200);
};

// ─ QR Code generator ─────────────────────────────────────────────
window.buildQR = function(containerId, seed) {
  const el = document.getElementById(containerId);
  if (!el) return;
  let h = 0;
  for (let i = 0; i < seed.length; i++) h = ((h << 5) - h + seed.charCodeAt(i)) | 0;
  let html = '';
  for (let i = 0; i < 100; i++) {
    const r = Math.floor(i/10), c = i%10;
    const isCorner = (r<3&&c<3)||(r<3&&c>6)||(r>6&&c<3);
    let filled;
    if (isCorner) filled = true;
    else { h = (Math.imul(h,1664525)+1013904223)|0; filled = (h>>>0)%2===0; }
    html += `<div class="qr-cell" style="background:${filled?'#111':'#fff'}"></div>`;
  }
  el.innerHTML = html;
};

// ─ Barcode generator ─────────────────────────────────────────────
window.buildBarcode = function(containerId) {
  const el = document.getElementById(containerId);
  if (!el) return;
  const hs = [24,12,30,16,24,8,34,20,14,28,10,24,18,32,12,24,8,30,18,26,14,30,10,24,16,32,12,26,18,24,10,32,20,14,28,10,24,18,32,12,24,8,34,20,16,28,12,24,16,32];
  el.innerHTML = hs.map(h => `<div class="bar-line" style="width:${h%2===0?2:3}px;height:${h}px"></div>`).join('');
};

// ─ Toast ─────────────────────────────────────────────────────────
window.showToast = function(msg) {
  let t = document.getElementById('toast-msg');
  if (!t) {
    t = document.createElement('div'); t.id='toast-msg';
    t.style.cssText='position:fixed;bottom:24px;left:50%;transform:translateX(-50%);background:#1e1e28;border:1px solid rgba(227,28,35,0.35);color:#ff6b6b;padding:11px 22px;border-radius:50px;font-size:13px;font-weight:600;z-index:999;box-shadow:0 8px 28px rgba(0,0,0,0.5);animation:fadeUp .3s ease;white-space:nowrap;';
    document.body.appendChild(t);
  }
  t.textContent = msg; t.style.display='block';
  clearTimeout(t._t);
  t._t = setTimeout(() => t.style.display='none', 2600);
};

// ─ Stagger card animations ───────────────────────────────────────
document.querySelectorAll('.movie-card').forEach((c, i) => {
  c.style.animationDelay = `${i * 0.065}s`;
});

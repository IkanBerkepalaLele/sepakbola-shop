(() => {
  const MAX = 4;          
  const GAP = 12;         

  function ensureHost() {
    let host = document.getElementById('toast-stack');
    if (!host) {
      host = document.createElement('div');
      host.id = 'toast-stack';
      host.className = 'fixed bottom-6 right-6 z-[9999] pointer-events-none';
      document.body.appendChild(host);
    }
    host.style.perspective = '1000px';
    if (!host._stack) host._stack = [];
    return host;
  }

  window.showToast = function (message, title, type = 'normal', duration = 3000) {
    const host = ensureHost();
    const stack = host._stack;

    const toast = document.createElement('div');
    toast.className = 'rounded-2xl p-4 pr-6 shadow-2xl flex items-center gap-3 pointer-events-auto';

    Object.assign(toast.style, {
      position: 'absolute', right: '0px', bottom: '0px',
      minWidth: '320px', maxWidth: '420px', width: 'max-content',
      transform: 'translateY(40px) scale(.98)', opacity: '0',
      transition: 'transform 300ms cubic-bezier(.2,.8,.2,1), opacity 300ms, filter 300ms',
      transformOrigin: 'center bottom'  
    });

    // ICON
    const iconWrap = document.createElement('div');
    iconWrap.className = 'w-8 h-8 flex items-center justify-center rounded-lg';
    const svg = (s)=>`<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">${s}</svg>`;
    const CHECK = svg('<path d="M6 12l4 4 8-8" stroke="white"/>');
    const CROSS = svg('<path d="M8 8l8 8M16 8l-8 8" stroke="white"/>');
    const INFO  = svg('<circle cx="12" cy="12" r="9"/><path d="M12 8h.01M12 12v4"/>');

    // TEXT
    const text = document.createElement('div');
    const h = document.createElement('h3');
    const p = document.createElement('p');
    h.className = 'font-semibold text-base';
    p.className = 'text-sm opacity-90';

    // TITLE
    if (type === 'success') h.textContent = 'Success';
    else if (type === 'error') h.textContent = 'Error';
    else h.textContent = title || '';

    p.textContent = message || '';

    if (type === 'success') {
      toast.classList.add('text-white','bg-gradient-to-r','from-emerald-400','to-green-500');
      iconWrap.classList.add('bg-white/20'); iconWrap.innerHTML = CHECK;
    } else if (type === 'error') {
      toast.classList.add('text-white','bg-gradient-to-r','from-orange-400','to-red-500');
      iconWrap.classList.add('bg-white/20'); iconWrap.innerHTML = CROSS;
    } else {
      toast.classList.add('bg-white','text-gray-900','border','border-gray-200');
      iconWrap.classList.add('bg-black/10'); iconWrap.innerHTML = INFO;
    }

    // tombol close
    const btn = document.createElement('button');
    btn.type = 'button'; btn.setAttribute('aria-label','Close');
    btn.className = 'ml-auto rounded-lg px-2 py-1 text-sm opacity-70 hover:opacity-100';
    btn.innerHTML = '&times;';

    text.append(h,p);
    toast.append(iconWrap, text, btn);
    host.appendChild(toast);
    stack.unshift(toast);

    layout();

    requestAnimationFrame(() => {
      toast.style.transform = 'translateY(0px) scale(1)';
      toast.style.opacity = '1';
    });

    let timer = setTimeout(hide, duration);
    toast.addEventListener('mouseenter', () => clearTimeout(timer));
    toast.addEventListener('mouseleave', () => (timer = setTimeout(hide, 800)));
    btn.addEventListener('click', () => hide(true));

    function hide() {
      clearTimeout(timer);
      toast.style.transform = 'translateY(20px) scale(.98)';
      toast.style.opacity = '0';
      toast.style.filter = 'blur(1px)';
      setTimeout(() => {
        const i = stack.indexOf(toast);
        if (i > -1) stack.splice(i, 1);
        toast.remove();
        layout();
      }, 250);
    }

    function layout() {
      while (stack.length > MAX) {
        const old = stack.pop();
        old?.remove();
      }

      const baseW = (stack[0]?.offsetWidth || 360) + 'px';
      stack.forEach(el => (el.style.width = baseW));

      //COMPOUNDING EFFECT
      stack.forEach((el, i) => {
        const y = i * (GAP + 4);            
        const s = 1 - i * 0.04;             
        const o = 1 - i * 0.18;              
        el.style.zIndex = String(9999 - i);  
        el.style.transformOrigin = 'bottom right';
        el.style.transform = `translateY(-${y}px) translateZ(${-i * 20}px) scale(${s})`;
        el.style.opacity = `${o}`;
        el.style.filter = `blur(${i * 0.3}px)`;
      });
    }
  };
})();

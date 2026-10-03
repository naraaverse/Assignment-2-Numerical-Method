def jacobi_method():
    # Deklarasi Nilai Awal dan Parameter
    v1, v2, v3 = 0.0, 0.0, 0.0
    toleransi_persen = 0.01
    max_iter = 100

    print("-" * 85)
    print(f"{'Iter (k)':<10} | {'V1(k)':<10} | {'V2(k)':<10} | {'V3(k)':<10} | {'Err V1 (%)':<10} | {'Err V2 (%)':<10} | {'Err V3 (%)':<10}")
    print("-" * 85)
    
    # Iterasi ke-0 (Nilai Awal)
    print(f"{0:<10} | {v1:<10.4f} | {v2:<10.4f} | {v3:<10.4f} | {'-':<10} | {'-':<10} | {'-':<10}")

    # Proses Iterasi
    for k in range(1, max_iter + 1):
        # Simpan nilai dari iterasi sebelumnya
        v1_lama, v2_lama, v3_lama = v1, v2, v3
        
        # Hitung nilai baru menggunakan persamaan KCL
        v1 = (7 + 2 * v2_lama + v3_lama) / 10
        v2 = (5 + v1_lama + 2 * v3_lama) / 8
        v3 = (12 + 2 * v1_lama + v2_lama) / 9
        
        # Hitung persentase relative error
        err_v1 = abs((v1 - v1_lama) / v1) * 100 if v1 != 0 else 0
        err_v2 = abs((v2 - v2_lama) / v2) * 100 if v2 != 0 else 0
        err_v3 = abs((v3 - v3_lama) / v3) * 100 if v3 != 0 else 0
        
        error_maks = max(err_v1, err_v2, err_v3)
        
        # Cetak hasil iterasi
        print(f"{k:<10} | {v1:<10.4f} | {v2:<10.4f} | {v3:<10.4f} | {err_v1:<10.2f} | {err_v2:<10.2f} | {err_v3:<10.2f}")
        
        # Cek Konvergensi
        if error_maks < toleransi_persen:
            print("-" * 85)
            return

    # Jika mencapai max_iter tapi belum konvergen
    print("-" * 85)
    print("Program mencapai maksimum iterasi (belum konvergen).")

if __name__ == "__main__":
    jacobi_method()
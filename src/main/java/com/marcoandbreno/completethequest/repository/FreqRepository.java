package com.marcoandbreno.completethequest.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import java.util.List;
import com.marcoandbreno.completethequest.model.Freq;

@Repository
public interface FreqRepository extends JpaRepository<Freq, Long> {
    List<Freq> findByUserId(Long userId);

}
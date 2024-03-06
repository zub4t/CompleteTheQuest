package com.marcoandbreno.completethequest.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import com.marcoandbreno.completethequest.common.UserPointsDTO;
import com.marcoandbreno.completethequest.model.UserPoints;
import java.util.List;
import java.util.Optional;
public interface UserPointsRepository extends JpaRepository<UserPoints, Long> {

    @Query("SELECT new com.marcoandbreno.completethequest.common.UserPointsDTO(u.username, up.points) FROM UserPoints up JOIN up.user u")
    List<UserPointsDTO> findAllUserPointsWithUsernames();

    Optional<UserPoints> findByUserId(Long userId);
}

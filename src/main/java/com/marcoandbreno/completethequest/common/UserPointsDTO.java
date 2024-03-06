package com.marcoandbreno.completethequest.common;

public class UserPointsDTO {
    private String username;
    private Integer points;

    // Constructors, getters, and setters

    public UserPointsDTO(String username, Integer points) {
        this.username = username;
        this.points = points;
    }
    
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public Integer getPoints() {
        return points;
    }

    public void setPoints(Integer points) {
        this.points = points;
    }
}
